import React from 'react';
import "./Main.scss"
import axios from 'axios'


class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
      resimageURL:'',
      doneProcess: false,
      processing: false,
      errorMessage:'',
      exeTime: ''
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }
  
  handleUploadImage(ev) {
    this.setState({
      processing: true
    })

    ev.preventDefault();

    const data = new FormData();

    console.log(this.uploadInput);
    console.log(this.numberInput.value);
    
    if (this.uploadInput.files[0] != null){
      
      const fileName = this.uploadInput.files[0].name;
      console.log(fileName)
      if (fileName.includes(".png") || fileName.includes('.jpg') || fileName.includes('.jpeg')){
        data.append('file', this.uploadInput.files[0]);
        data.append('filename', this.uploadInput.files[0].name);
        
        if(this.numberInput.value < 0 || this.numberInput.value > 100) {
          this.setState({
            errorMessage: 'Compression Rate hanya bisa 0 sampai 100',
            processing: false
          })
        } else {
          this.setState({
            errorMessage: ''
          })
          data.append('compression_rate',this.numberInput.value);
        
          fetch('/upload', {
            method: 'POST',
            body: data,
          }).then((response) => {
      
              if(response.status === 200){
                  this.setState({ 
                    imageURL: `http://127.0.0.1:5000/static/test_docs/${fileName}`,
                    resimageURL: `http://127.0.0.1:5000/static/hasil/compressed_${fileName}`,
                    doneProcess: true,
                    processing: false,
                    errorMessage:''
                });

                fetch('time').then(res => res.json()).then(d => {
                  this.setState({
                    exeTime: d.time
                  })
                })
              }
          });
        }
      }else{
        this.setState({
          processing: false,
          errorMessage: 'Format file tidak valid'
        })
      }
    }else{
      this.setState({
        processing: false,
        errorMessage: 'Belum ada file yang di upload'
      }) 
    }
    
  }

  download_file = e => {
    e.preventDefault();
    if (this.uploadInput.files[0] != null){
      axios({
        url: this.state.resimageURL,
        method: 'GET',
        responseType: 'blob', // important
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        console.log(this.fileName)
        link.setAttribute('download', 'compressed_'+this.uploadInput.files[0].name);
        document.body.appendChild(link);
        link.click();
      });
    }
    
  }
  
  
  render() {
    return (
        <div>
          <form onSubmit={this.handleUploadImage} className="input-wrapper">
            <div className="input-header">
              <p className="input-title">Input Your Image</p>
              <div className="input-file">
                <input ref={(ref) => { this.uploadInput = ref; }} type="file" required />
              </div>
              <div className="compression-wrapper">
                <p className="compression-text">Image Compression Rate : </p>
                <input className="compression-input" ref={(ref) => {this.numberInput = ref; }} type='text' name="compression_rate" required />
              </div>
              <button className={this.state.processing ? "input-button-hidden" : "input-button"}>Compress</button>
              <p className="input-error">{this.state.errorMessage}</p>
            </div>
          
            <div className={this.state.doneProcess ? "result-wrapper" : "result-wrapper-hidden"}>
              <div className="result-image">
                <div className="result-before">
                  <p>Before</p>
                  <img src={this.state.imageURL} alt="img" width="350px" />
                </div>
                <div className="result-after">
                  <p>After</p>
                  <img src={this.state.resimageURL} alt="img" width="350px" />
                </div>
              </div>
              <button className="result-button" onClick={this.download_file}>Download</button>
              <div className="result-sum">
                <p className="result-pixel">Perbedaan Pixel: ?</p>
                <p className="result-time">Waktu Eksekusi: {this.state.exeTime}</p>
              </div>
            </div>
          </form>
        </div>
    );
  }
}

export default Main;