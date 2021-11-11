import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
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
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <p>{this.state.errorMessage}</p>
        <input ref={(ref) => {this.numberInput = ref; }} type='text' name="compression_rate" placeholder="Compression Rate"/>
        <div>
          <button>Upload</button>
        </div >
        <img src={this.state.imageURL} alt="img" width='300px' />
      </form>
    );
  }
}

export default Main;