import React from 'react';
import "./Main.scss"

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
      resimageURL:'',
      errorMessage:''
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();

    console.log(this.uploadInput);
    console.log(this.numberInput.value);
    if (this.uploadInput.files[0] != null){
      
      const fileName = this.uploadInput.files[0].name;
      if (fileName.includes(".png") || fileName.includes('.jpg') || fileName.includes('.jpeg')){
        data.append('file', this.uploadInput.files[0]);
        data.append('filename', this.uploadInput.files[0].name);
        data.append('compression_rate',this.numberInput.value);
    
        fetch('/upload', {
          method: 'POST',
          body: data,
        }).then((response) => {
    
            if(response.status === 200){
                this.setState({ 
                  imageURL: `http://127.0.0.1:5000/static/test_docs/${fileName}`,
                  resimageURL: `http://127.0.0.1:5000/static/hasil/compressed_${fileName}`,
                  errorMessage:''
              });
            }
        });
      }else{
        this.setState({
          errorMessage: 'Format file tidak valid'
        })
      }
    }else{
      this.setState({
        errorMessage: 'Belum ada file yang di upload'
      })
      
    }
    
  }

  render() {
    return (
        <form onSubmit={this.handleUploadImage} className="input-wrapper">
          <div className="input-header">
            <p className="input-text">Input Your Image</p>
            <div className="input-file">
              <input ref={(ref) => { this.uploadInput = ref; }} type="file" required />
            </div>
            <div className="compression-wrapper">
              <p className="compression-text">Image Compression Rate : </p>
              <input className="compression-input" ref={(ref) => {this.numberInput = ref; }} type='text' name="compression_rate" required />
            </div>
            <button className="input-button">Compress</button>
          </div>
          <p className="input-error">{this.state.errorMessage}</p>
          
          <img src={this.uploadInput} alt="img" width='300px' />
          <img src={this.state.resimageURL} alt="img" width='300px'/>
        </form>
    );
  }
}

export default Main;