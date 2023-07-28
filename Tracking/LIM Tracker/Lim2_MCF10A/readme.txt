
1. File Description
(1) GT_MaskImage
		Ground-truth images created by this software for evaluation.

(2) Lim2_Result.limpj
		The tracking results after applying Detection & Link-type tracking function.
		Only the windows version is supported.



2. How to restore the tracking results
(1) Unzip Lim2_MCF10A.zip and copy it directly under the C drive (e.g., C:/Lim2_MCF10A).

(2) Download the following file and save it directly under the C:/Lim2_MCF10A folder.
	https://ssbd.riken.jp/data/ssbd-000216/repos/Fig%202/BG-Reg-BG-iRFP_G02_s4_207.tif

(3) Launch Fiji and select "Plugins/Tracking/LIM Tracker Plugin" from the menu while no images are loaded.
	-> The message "There are no images open" will appear. Click the OK button.

(4) Select "Lim2_Result.limpj" in the file dialog.
	-> The tracking result will restore.



3. Parameters
(1) Detect: 
		Frame 0-59, 	Threshold=2000, CellSize=22, Dilation=ON
		Frame 60-99, 	Threshold=1200, CellSize=22, Dilation=ON
		Frame 100-206, 	Threshold=1000, CellSize=22, Dilation=ON

(2) LinkROIs: 
		LinkROIRange=60, LinkSplitTrack=60, FillFrameGap=0

(3) Apply "Realign ID numbers"