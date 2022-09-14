
import './App.css';
import Predict from './Predict';


function App() {
  const PageStyle = {
    margin:'auto',
    width: "100vw",
    alignItems: 'center',
    justifyContent: 'center',

  }
  return (
    <div className="App" style={PageStyle}>
      <p>This app predicts the whther a slide is Invasive Ductal Carcinoma or not!</p>
      <Predict/>
    </div>
  );
}

export default App;
