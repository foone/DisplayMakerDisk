import struct,sys
filename=sys.argv[1]
with open(sys.argv[1],'rb') as f:
	data=f.read()

ENTRYSIZE=18
BLANKNAMES=(
	'            ',
	'\0           '
)
DISK_SIGNATURE='AMCOR ELECTRONICS LTD. DISKETTE PROJECTRON'
DISK_TYPES={
	15:(0x3A00,0x3C00),
	16:(0x3C00,0x4000)
}
def determine_disk_type(data):
	for sectors_per_track,(signature_offset,directory_offset) in DISK_TYPES.items():
		if data[signature_offset:signature_offset+len(DISK_SIGNATURE)]==DISK_SIGNATURE:
			return sectors_per_track

def calculate_offset(disk_type, sector_num):
	# offset 0 starts on cylinder 1, so we need two tracks of sectors before it
	track_1_start = disk_type * 2 
	if disk_type == 16:
		# Convert the 15-sector based offset to a 16-sector offset.
		track = sector_num // 15
		sector = sector_num % 15
		sector_num = 16 * track + sector
	return 512*(sector_num+track_1_start)

disk_type = determine_disk_type(data)
if disk_type is None:
	print 'Unknown disk type! Assuming it\'s a dumped file table'
	DIRECTORY_OFFSET=0
else:
	print 'Disk type: {} sector'.format(disk_type)
	DIRECTORY_OFFSET=DISK_TYPES[disk_type][1]

tlengths=0
for i in range(256):
	offset=DIRECTORY_OFFSET+ENTRYSIZE*i
	entry = data[offset:offset+ENTRYSIZE]
	name,start,length,u1,u2,u3=struct.unpack('<12sHBBBB',entry)
	if name in BLANKNAMES:
		continue
	file_offset = calculate_offset(disk_type, start)
	if i==0:
		print 'Volume  : "{}", {: 3d} blocks used, {: 3d} files. Unknowns: 1={:02X} 2={:02X} 3={:02X}'.format(name,start,length,u1,u2,u3)
	else:
		print 'File {: 3d}: "{}", {: 3d} blocks, start at {:3d} (byte offset 0x{:06x}). Unknowns: 1={:02X} 2={:02X} 3={:02X}'.format(i,name,length,start,file_offset,u1,u2,u3)
