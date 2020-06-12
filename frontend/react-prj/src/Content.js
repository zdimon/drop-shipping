import React from 'react';

import './App.css';


export class Content extends React.Component {

    name = 'Dimadsfsdfsdfdsfsd';

    users = [
        {name: 'Dima'},
        {name: 'Vova'}
    ]

    

  constructor(props){
    super(props);
    this.state = {users: this.users, name: this.name};
  }
  
  doClick = async () => {
      await this.setState({name: 'Nikitos'});
      this.props.handleClick(this.state.name);
      // this.state.name = 'Test';
      // this.forceUpdate();
  }

  render() {

      

      return <div className="content">
          content
            {/* {this.users.map((i) => <div>{i}</div>)} */}

            {this.state.users.map((i) => <div>{i.name}</div>)}

            {this.state.name}

            <button onClick={this.doClick}>click</button>
        </div>
      
    }    
  
}

