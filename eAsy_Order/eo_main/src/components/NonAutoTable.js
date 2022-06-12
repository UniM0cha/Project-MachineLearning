import React, {useMemo} from "react"

import Productlist from "../jsonData/Productlist.json"


// export const BasicTable = () =>{

//     const columns = useMemo(() => COLUMNS, [])
//     const data = useMemo(() => Productlist, [])
  
//     //ES6 에서는 꼭 이렇게 key값이랑 매칭 안해줘도 변수명이 같으면 알아서 잘 들어감!
//     // const tableInstance = useTable({ columns : columns, data : data })
//     const tableInstance = useTable({columns, data})
  
//     return (
//         <table {...getTableProps()} id='customers'>
//           <thead>
//             {headerGroups.map((headerGroup) => (
//               <tr {...headerGroup.getHeaderGroupProps()}>
//                 {headerGroup.headers.map((column) => (
//                   <th {...column.getHeaderProps()}>{column.render("Header")}</th>
//                 ))}
//               </tr>
//             ))}
//           </thead>
//           <tbody {...getTableBodyProps()}>
//             {rows.map((row) => {
//               prepareRow(row);
//               return (
//                 <tr {...row.getRowProps()}>
//                   {row.cells.map((cell) => {
//                     return <td {...cell.getCellProps()}>{cell.render("Cell")}</td>;
//                   })}
//                 </tr>
//               );
//             })}
//           </tbody>
//         </table>
//       );
//   }

function NonAutoTable() {
    const column = Object.keys(Productlist[0]);
    const thData = () => {
        return column.map((data) => {
            return<th key = {data}>{data}</th>
        })
    }

    const tdData = () => {
        return Productlist.map((data) =>{ return(
            <tr>
                {
                    column.map((v) => {
                        return <td>{data[v]}</td>
                    })
                }
            </tr>
        )
    })
       
    }
    return(
        <table className="cumtomers">
        <thead>
         <tr>{thData()}</tr>
        </thead>
        <tbody>
        {tdData()}
        </tbody>
       </table>
    )
}

export default NonAutoTable;