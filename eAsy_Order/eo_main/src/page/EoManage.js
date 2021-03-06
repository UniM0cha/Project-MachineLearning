import React from "react";

// 헤더
import Header from "../components/Header";
// 엑셀 데이터
import SheetManage from "../components/sheetManage";

const EoManageNA = () => {

  const mainGo = () => {
    window.location.href = '/main';
  }

  return(
    <div>
      <div><Header/></div>
      <div className="fonth1">발주 내역 확인</div>
      <div className="mainParents"><SheetManage/></div>
      <div className='buttonhi'><button onClick={mainGo} className="buttonhi"  >돌아가기</button></div>
    </div>

  )
}

export default EoManageNA;