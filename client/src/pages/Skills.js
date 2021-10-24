import React, {useMemo, useState, useEffect } from 'react';
import { makeRenderer, useTable } from "react-table";
import '../styles/tableCSS.css';

const Skills = () => {

  const [tableData, setTableData] = useState([]);
  const [tableColumns, setTableColumns] = useState([]);

  useEffect(() => {
      fetch('/skills').then(res => res.json()).then(data => {
          setTableData( data.tableData );
          setTableColumns( data.tableColumns );
          });
      }, []);

  const data = React.useMemo(() => tableData, [tableData]);
  const columns = React.useMemo(() => tableColumns, [tableColumns]);

  const {
            getTableProps,
            getTableBodyProps,
            headerGroups,
            rows,
            prepareRow
        } = useTable({ columns, data });




  return (
    <html>
    
    <h1 class ="h1">Skills </h1>

      <body>
          <div class="center_header">
          
            <table class="center" {...getTableProps()} style={{ border: 'solid 1px blue' }}>
              <thead>
                {headerGroups.map(headerGroup => (
                  <tr {...headerGroup.getHeaderGroupProps()}>
                    {headerGroup.headers.map(column => (
                        <th
                          {...column.getHeaderProps()}
                  style={{
                  borderBottom: 'solid 3px blue',
                  background: 'aliceblue',
                  color: 'black',
                  fontWeight: 'bold',
                  }}
              >
                {column.render('Header')}
                  </th>
                ))}
              </tr>
              ))}
            </thead>
            <tbody {...getTableBodyProps()}>
            {rows.map(row => {
              prepareRow(row)
              return (
              <tr {...row.getRowProps()}>
              {row.cells.map(cell => {
              return (
                <td
                  {...cell.getCellProps()}
                    style={{
                    padding: '10px',
                    border: 'solid 1px gray',
                    background: 'white',
                    }}
                  >
                  {cell.render('Cell')}
                  </td>
                  )
                  })}
                </tr>
              )
              })}
            </tbody>
            </table>
          </div>
      </body>
  </html>    

  );
};
  
export default Skills;
