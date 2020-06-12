import React from 'react';

import './App.css';

import { Content } from './Content'

class App extends React.Component {
  constructor(props){
    super(props);
  }

  doDo(mv){
    console.log(mv);
  }

  render() {
      return <div className="App">
          <header className="App-header">
            header
          </header>

          <div>
            <Content handleClick={this.doDo} />
          </div>

        </div>
      
    }    
  
}



export default App;
