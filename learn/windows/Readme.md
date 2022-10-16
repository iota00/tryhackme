# Windows

## Windows Fondamental

## Windows Editions

1. What encryption can you enable on Pro that you can't enable in Home?

```
BitLocker
```

## GUI

1. Which selection will hide/disable the Search box?

```
hidden
```

2. Which selection will hide/disable the Task View button?

```
Show Task View button
```

3. Besides Clock, Volume, and Network, what other icon is visible in the Notification Area?


```
action center
```

## File System

* The file system used in modern versions of Windows is the ```New Technology File System``` or simply ```NTFS```.
* Before NTFS, there was FAT16/FAT32 (File Allocation Table) and HPFS (High Performance File System).
* NTFS (aka journaling file system) In case of a failure, the file system can automatically repair the folders/files on disk using information stored in a log file. This function is not possible with FAT.  
* NTFS addresses many of the limitations of the previous file systems; such as:
    * Supports files larger than 4GB
    * Set specific permissions on folders and files
    * Folder and file compression
    * Encryption (Encryption File System or EFS)

* On NTFS volumes, you can set permissions that grant/deny access to files/folders. The permissions are:

    * Full control
    * Modify
    * Read & Execute
    * List folder contents
    * Read
    * Write
* **Alternate Data Streams (ADS)** (another feature of NTFS): a file attribute specific to Windows **NTFS**. 
* Every file has at least one **data stream** ($DATA), and ADS allows files to contain more than one stream of data. Use *3rd party executables* or *powershell* to view this data (ADS for files).



1. What is the meaning of NTFS?

```
New Technology File System
```

## Windows\System32 Folders

* The Windows folder ```C:\Windows``` is traditionally known as the folder which contains the Windows operating system. 
* This is where environment variables(**system environment variables**), come into play. The system  environment variable for the *Windows directory* is ```%windir%```.

> Per Microsoft, "Environment variables store information about the operating system environment. This information includes details such as the operating system path, the number of processors used by the operating system, and the location of temporary folders".

* The ```System32``` folder holds the important files that are critical for the operating system.

> Note: Many of the tools that will be covered in the Windows Fundamentals series reside within the System32 folder. 

1. What is the system variable for the Windows folder?

```
%windir%
```