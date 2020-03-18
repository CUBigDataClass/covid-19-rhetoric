import React, {useState,useEffect} from 'react';
import logo from './logo.svg';
import './App.css';
import { TwitterTimelineEmbed, TwitterShareButton, TwitterFollowButton, TwitterHashtagButton, TwitterMentionButton, TwitterTweetEmbed, TwitterMomentShare, TwitterDMButton, TwitterVideoEmbed, TwitterOnAirButton } from 'react-twitter-embed';



export default class App extends React.Component {

  constructor(props){
    super(props)
    this.state = {time : '0'}
  }

  componentDidMount(){
    var vm = this;
    setInterval(()=>{
      fetch('/time').then(res => res.json()).then(data => {
        vm.setState({
          time: data.time
        });
      })
    })
  }
  render(){
    var vm = this;
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
          <p>The current time is {vm.state.time}</p>
          <p>
  
          <TwitterTweetEmbed
          tweetId={'1203753948173094913'}
  />
          </p>
        </header>
  
        
        
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
