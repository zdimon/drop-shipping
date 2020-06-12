import { Component, OnInit, EventEmitter } from '@angular/core';

import { ViewChild } from '@angular/core';

import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.scss']
})
export class CameraComponent implements OnInit {


  @ViewChild('hardwareVideo', {static: true}) hardwareVideo: any;
  @ViewChild('canvas', {static: true}) canvas: any;
  _navigator = navigator as any;
  localStream;
  image_data: any;

  onPic = new EventEmitter();

  constructor(public dialogRef: MatDialogRef<CameraComponent>,) { }

  ngOnInit() {
    this.getVideo();
  }

  getVideo() {

    const video = this.hardwareVideo.nativeElement;
    this._navigator =  navigator as any;

    this._navigator.getUserMedia = ( this._navigator.getUserMedia || this._navigator.webkitGetUserMedia
    || this._navigator.mozGetUserMedia || this._navigator.msGetUserMedia );

    this._navigator.mediaDevices.getUserMedia({video: { width: 400,  height: 300 }, audio: false})
      .then((stream) => {
        this.localStream = stream;
        video.srcObject = stream;
        video.play();
    });

  }

  stopStream() {
    const tracks = this.localStream.getTracks();
    tracks.forEach((track) => {
      track.stop();
    });

  }

  takePic() {
    const context = this.canvas.nativeElement.getContext('2d');
    context.drawImage(this.hardwareVideo.nativeElement, 0, 0, 400, 300);
    const dataURL = this.canvas.nativeElement.toDataURL();
    this.image_data = {imgBase64: dataURL};
    this.onPic.next(this.image_data);
    this.stopStream();
    this.dialogRef.close();

  }


}
