import React, {useMemo, useState, useEffect } from 'react';
import { makeRenderer, useTable } from "react-table";
import Sidebar from "./components/Sidebar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import AppliedJobs from "./pages/AppliedJobs";
import Companies from "./pages/Companies";
// import { Companies, CompaniesOne, CompaniesTwo } from "./pages/Companies";
import Contacts from "./pages/Contacts";
import Skills from "./pages/Skills";
import Login from "./pages/Login";
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';


function App() {

  const [currentMsg, setCurrentMsg] = useState(0);
  const [tableData, setTableData] = useState([]);

  useEffect(() => {
	       fetch('/welcome_msg').then(res => res.json()).then(data => {
		               setCurrentMsg(data.msg);
		            });
	    }, []);

  // FOR SOME REASON THE BELOW WAS BRINGING UP A LOG ERROR...

  // useEffect(() => {
	//        fetch('/table').then(res => res.json()).then(data => {
	// 	               setTableData( data.tableData );
	// 	            });
	//     }, []);
   
  const data = React.useMemo(() => tableData, [tableData]);

  const columns = React.useMemo(
	      () => [
		        {
			    Header: "Column 1",
			    accessor: "col1"
			},
		        {
			    Header: "Column 1",
			    accessor: "col2"
				          }
		    ],
	      []
	    ); 

  const {
            getTableProps,
	    getTableBodyProps,
	    headerGroups,
	    rows,
	    prepareRow
        } = useTable({ columns, data });


  return (
    <Router>
      <Sidebar />
      <Switch>
        <Route path="/" exact component={Login} /> {/* the home page */}
        <Route path="/applied_jobs" exact component={AppliedJobs} />
        <Route path="/contacts" exact component={Contacts} />
        <Route path="/companies" exact component={Companies} />
        <Route path="/skills" exact component={Skills} />
        <Route path="/login" exact component={Login} />
      </Switch>
  </Router>
  );
}

export default App;


// Kept everything from below. Still need to figure out how to incorportate the table Matthew started. 
    
  
//   );
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>

  //       <p> {currentMsg}. </p>
  //       <p>{JSON.stringify(data)}</p>

  //    <table {...getTableProps()} style={{ border: 'solid 1px blue' }}>
  //      <thead>
  //        {headerGroups.map(headerGroup => (
  //          <tr {...headerGroup.getHeaderGroupProps()}>
  //            {headerGroup.headers.map(column => (
  //              <th
  //                {...column.getHeaderProps()}
  //                style={{
  //                  borderBottom: 'solid 3px red',
  //                  background: 'aliceblue',
  //                  color: 'black',
  //                  fontWeight: 'bold',
  //                }}
  //              >
  //                {column.render('Header')}
  //              </th>
  //            ))}
  //          </tr>
  //        ))}
  //      </thead>
  //      <tbody {...getTableBodyProps()}>
  //        {rows.map(row => {
  //          prepareRow(row)
  //          return (
  //            <tr {...row.getRowProps()}>
  //              {row.cells.map(cell => {
  //                return (
  //                  <td
  //                    {...cell.getCellProps()}
  //                    style={{
  //                      padding: '10px',
  //                      border: 'solid 1px gray',
  //                      background: 'papayawhip',
  //                    }}
  //                  >
  //                    {cell.render('Cell')}
  //                  </td>
  //                )
  //              })}
  //            </tr>
  //          )
  //        })}
  //      </tbody>
  //    </table>

	// </header>
  //   </div>


  // );
  //  }

// export default App;
