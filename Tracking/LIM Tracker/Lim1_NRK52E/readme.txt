
1. File Description
(1) GT_MaskImage
		Ground-truth images created by this software for evaluation.

(2) Lim1_Result.limpj
		The tracking results after applying Detection & Link-type tracking function.
		Only the windows version is supported.



2. How to restore the tracking results
(1) Unzip Lim1_NRK52E.zip and copy it directly under the C drive (e.g., C:/Lim1_NRK52E).

(2) Download the following file and save it directly under the C:/Lim1_NRK52E folder.
	https://ssbd.riken.jp/data/ssbd-000216/repos/Fig%201/BG-CFP-BG-FRET_kept_stack_217.tif

(3) Launch Fiji and select "Plugins/Tracking/LIM Tracker Plugin" from the menu while no images are loaded.
	-> The message "There are no images open" will appear. Click the OK button.

(4) Select "Lim1_Result.limpj" in the file dialog.
	-> The tracking result will restore.



3. Parameters
(1) Detect: 
		AllFrames, 	Threshold=4000, CellSize=9, Dilation=ON

(2) LinkROIs: 
		LinkROIRange=20, LinkSplitTrack=20, FillFrameGap=0

(3) Apply "Realign ID numbers"