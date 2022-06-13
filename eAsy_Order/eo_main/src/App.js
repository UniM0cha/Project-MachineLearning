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
import Axiostest from './page/Axiostest';
import EoManageNA from './page/EoManageNonAuto';


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
        {/* 발주 세부 경로 */}
        <Route path="/manage" element={<EoManage />}></Route>
      </Routes>
      <Routes>
        {/* 발주 세부 경로 */}
        <Route path="/managena" element={<EoManageNA />}></Route>
      </Routes>
      <Routes>
        {/* 발주 경로 */}
        <Route path="/balju" element={<EoBalju />}></Route>
      </Routes>
      <Routes>
        {/*  test 경로*/}
        <Route path="/testest" element={<Axiostest />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
