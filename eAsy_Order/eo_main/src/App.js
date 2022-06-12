import './App.css';

// bootstrap 테마 사용. 
import 'bootstrap/dist/css/bootstrap.min.css';

// route
import { BrowserRouter, Routes, Route} from "react-router-dom";

// page
import EoMain from './page/EoMain';
import EoBalju from './page/EoBalju';
import EoLogin from './page/EoLogin';
import EoManage from './page/EoManage';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* 기본 경로 = login */}
        <Route path="/" element={<EoLogin />}></Route>
      </Routes>
      <Routes>
        {/* 메인페이지 */}
        <Route path="/main" element={<EoMain />}></Route>
      </Routes>
      <Routes>
        {/* 발주 경로 */}
        <Route path="/admin" element={<EoManage />}></Route>
      </Routes>
      <Routes>
        {/* 관리 경로 */}
        <Route path="/balju" element={<EoBalju />}></Route>
      </Routes>

    </BrowserRouter>
  );
}

export default App;
