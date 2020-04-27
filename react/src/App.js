import React, { useState, useEffect } from 'react';
import './CSS/App.css';


export default class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = { tweetIds: [] }
  }

  componentDidMount() {
    var vm = this;
    fetch('/GetTopPostsState/CO').then(res => res.json()).then(data => {
      console.log(data)
    })
  }

  render() {
    return (
      <div className="App">
        <h1>"Hello World!</h1>
      </div>
    );
  }
}


// function App() {

//   const [currentTime,setCurrentTime] = useState(1)
//   useEffect(()=>{
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time)
//     });
//   },[]);
//   return (
//     <div className="App">
//       <header className="App-header">
//         {/* <img src={logo} className="App-logo" alt="logo" /> */}
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//         <p>The current time is {currentTime}</p>
//         <p>

//         <TwitterTweetEmbed
//         tweetId={'1203753948173094913'}
// />
//         </p>
//       </header>



//     </div>
//   );
// }

// export default App;
