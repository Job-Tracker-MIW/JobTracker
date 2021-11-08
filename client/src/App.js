import React, {useMemo, useState, useEffect } from 'react';
import { makeRenderer, useTable } from "react-table";
import Sidebar from "./components/Sidebar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import AppliedJobs from "./pages/AppliedJobs/AppliedJobs";
import Companies from "./pages/Companies";
// import { Companies, CompaniesOne, CompaniesTwo } from "./pages/Companies";
import Contacts from "./pages/Contacts/Contacts";
import Skills from "./pages/Skills/Skills";
import Login from "./pages/Login/Login";
import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [currentMsg, setCurrentMsg] = useState(0);
  const [tableData, setTableData] = useState([]);
  const [token, setToken] = useState(localStorage.getItem('token'));


  useEffect(() => {
	       fetch('/welcome_msg').then(res => res.json()).then(data => {
		               setCurrentMsg(data.msg);
		            });
	    }, []);
   
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

  if(!token) {
    return (
      <Login setToken={setToken}></Login>
    );
  }

  return (
    <Router>
      <Sidebar setToken={setToken}/>
      <Switch>
        <Route path="/" exact component={AppliedJobs} /> {/* the home page */}
        <Route path="/applied-jobs-page" exact component={AppliedJobs} />
        <Route path="/contacts-page" exact component={Contacts} />
        <Route path="/companies-page" exact component={Companies} />
        <Route path="/skills-page" exact component={Skills} />
        <Route path="/login-page" exact component={Login} />
      </Switch>
  </Router>
  );
}

export default App;
