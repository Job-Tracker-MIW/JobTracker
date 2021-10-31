import React, {useMemo, useState, useEffect } from 'react';
import { makeRenderer, useTable } from "react-table";
import Sidebar from "./components/Sidebar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import AppliedJobs from "./pages/AppliedJobs";
import Companies from "./pages/Companies/Companies";
import Contacts from "./pages/Contacts";
import Skills from "./pages/Skills/Skills";
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


