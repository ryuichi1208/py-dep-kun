## ADD
if [ $UID != 0 ]
then
	echo "FAILED: Must have root access to execute this script"
	exit 1
fi

while getopts h:d:t: args
do
	case $args in
	h)	NFS_SERVER=$OPTARG ;;
	d)	REM_DISK_PART=$OPTARG ;;
	t)	FS_TYPE=$OPTARG ;;
	\?)	echo $USAGE ; exit 1 ;;
	esac
done

if [ -z "$NFS_SERVER" ]
then
	echo $USAGE
	echo "FAILED: NFS Server not specificed"
	exit 1
fi

if [ -z "$REM_DISK_PART" ]
then
	echo $USAGE
	echo "FAILED: NFS Server disk partition not specified"
	exit 1
fi

if [ -z "$FS_TYPE" ]
then
	echo $USAGE
	echo "FAILED: NFS Server file system type not specified"
	exit 1
fi

#
# How to check if it a valid block special device on NFS Server ???
# Add code here.


ping -c 2 -w 15 $NFS_SERVER >/dev/null 2>&1
if [ $? != 0 ]
then
	echo "FAILED: ping $NFS_SERVER failed"
	exit 1
fi

rsh -n -l root $NFS_SERVER "ls -l /etc" >/dev/null 2>&1
if [ $? != 0 ]
then
	echo "FAILED: rsh -n -l root $NFS_SERVER "ls -l /etc" failed"
	exit 1
fi

rsh -n -l root $NFS_SERVER "rpm -q -a | grep $FS_TYPE" | grep $FS_TYPE >/dev/null 2>&1
if [ $? != 0 ]
then
	rsh -n -l root $NFS_SERVER "grep $FS_TYPE /etc/filesystems" | grep $FS_TYPE >/dev/null 2>&1
	if [ $? != 0 ]
	then
		rsh -n -l root $NFS_SERVER "grep $FS_TYPE /proc/filesystems" | grep $FS_TYPE >/dev/null 2>&1
		if [ $? != 0 ]
		then
			echo "FAILED: $FS_TYPE package is not installed or loaded on $NFS_SERVER"
			exit 1
		fi
	fi
fi

rsh -n -l root $NFS_SERVER "mkdir -p -m 777 $MNT_POINT"
if [ $? != 0 ]
then
	echo "FAILED: Could not mkdir -p -m 777 $MNT_POINT on $NFS_SERVER"
	exit 1
fi

rsh -n -l root $NFS_SERVER "mount -t $FS_TYPE $REM_DISK_PART $MNT_POINT"
if [ $? != 0 ]
then
	echo "FAILED: Could not mount -t $FS_TYPE $REM_DISK_PART on $MNT_POINT"
	exit 1
fi

rsh -n -l root $NFS_SERVER "chmod 777 $MNT_POINT"
if [ $? != 0 ]
then
	echo "FAILED: Could not chmod 777 $MNT_POINT on $NFS_SERVER"
	exit 1
fi

mkdir -p -m 777 $MNT_POINT
mount -t nfs $NFS_SERVER:$MNT_POINT $MNT_POINT
if [ $? != 0 ]
then
	echo "FAILED: NFS mount failed"
	exit 1
fi

mkdir -p -m 777 $MNT_POINT/test_dir

umount $MNT_POINT
rm -rf $MNT_POINT

rsh -n -l root $NFS_SERVER "/usr/sbin/exportfs -u :$MNT_POINT"
rsh -n -l root $NFS_SERVER "umount $MNT_POINT"
rsh -n -l root $NFS_SERVER "rm -rf $MNT_POINT"
echo "PASSED: $0 passed!"
exit 0
