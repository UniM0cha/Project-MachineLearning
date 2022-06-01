import './App.css';

// bootstrap 테마 사용. css는 가장 나중에 선언한 css가 적용됨
import 'bootstrap/dist/css/bootstrap.min.css';

// route
import { BrowserRouter, Routes, Route} from "react-router-dom";

// page
import EoMain from './page/EoMain';
import EoBalju from './page/EoBalju';
import Login from './page/Login';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* 기본 경로 = login */}
        <Route path="/" element={<Login />}></Route>
      </Routes>
      <Routes>
        {/* 기본 경로 = login */}
        <Route path="/main" element={<EoMain />}></Route>
      </Routes>
      <Routes>
        {/* 발주 경로 */}
        <Route path="/balju" element={<EoBalju />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
