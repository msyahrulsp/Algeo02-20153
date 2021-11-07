import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: '',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();


    const data = new FormData();

    const fileName = this.uploadInput.files[0].name;
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', this.uploadInput.files[0].name);

    fetch('/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {

        if(response.status === 200){
            this.setState({ imageURL: `http://127.0.0.1:5000/static/test_docs/${fileName}`});
        }
    });
  }

  render() {
    return (
      <form onSubmit={this.handleUploadImage}>
        <div>
          <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
        </div>
        <div>
          <input ref={(ref) => { this.fileName = ref; }} type="text" placeholder="Enter the desired name of file" />
        </div>
        <br />
        <div>
          <button>Upload</button>
        </div >
        <img src={this.state.imageURL} alt="img" width='300px' />
      </form>
    );
  }
}

export default Main;