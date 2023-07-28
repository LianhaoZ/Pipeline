
1. File Description
(1) GT_MaskImage
		Ground-truth images created by this software for evaluation.
		Based on the "01" folder images of the following data set.
		http://data.celltrackingchallenge.net/challenge-datasets/PhC-C2DH-U373.zip.

(2) Lim3_Result.limpj
		The tracking results after applying DL recognition & Link-type tracking function.
		Only the windows version is supported.



2. How to restore the tracking results
(1) Unzip Lim3_PhC-C2DH-U373.zip and copy it directly under the C drive (e.g., C:/Lim3_PhC-C2DH-U373).

(2) Download the following file, unzip it, and copy the "01" folder into the C:/Lim3_PhC-C2DH-U373 folder.
	http://data.celltrackingchallenge.net/challenge-datasets/PhC-C2DH-U373.zip.

(3) Launch Fiji and select "Plugins/Tracking/LIM Tracker Plugin" from the menu while no images are loaded.
	-> The message "There are no images open" will appear. Click the OK button.

(4) Select "Lim3_Result.limpj" in the file dialog.
	-> The tracking result will restore.



3. Parameters
	Apply DL recognition function "Matterport"
	LinkROIs: LinkROIRange=300, LinkSplitTrack=0, FillFrameGap=0