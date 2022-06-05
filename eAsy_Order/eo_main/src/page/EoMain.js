import React from 'react';

//haeder
import Header from '../components/Header';

// chart
import MyChart from '../components/Chart';


const EoMain = () => {
  return (
    <div>
      <div><Header /></div>
      <div className='mainParents'><MyChart/></div>
      
    </div>

  )


}

export default EoMain;