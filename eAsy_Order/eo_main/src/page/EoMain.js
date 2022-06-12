import React from 'react';

//haeder
import Header from '../components/Header';

// chart
import MyChart from '../components/Chart';

//sheets
import Sheets from '../components/Sheet';


const EoMain = () => {
  return (
    <div>
      <div><Header /></div>
      <div className='mainParents'><MyChart/></div>
      <div className='mainParents'><Sheets/>
     
      </div>
    </div>

  )


}

export default EoMain;