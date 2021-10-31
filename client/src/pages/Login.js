import React, { Component } from "react";
import { makeRenderer, useTable } from "react-table";
import '../styles/Login.css';



// const Companies = () => {
//     const [tableData, setTableData] = useState([]);
//     const [tableColumns, setTableColumns] = useState([]);
  
//     useEffect(() => {
//           fetch('/companies').then(res => res.json()).then(data => {
//             setTableData( data.tableData );
//             setTableColumns( data.tableColumns );
//             });
//           }, []);
  
//     const data = React.useMemo(() => tableData, [tableData]);
//     const columns = React.useMemo(() => tableColumns, [tableColumns]);
//     const {
//                getTableProps,
//                getTableBodyProps,
//                headerGroups,
//                rows,
//                prepareRow
//           } = useTable({ columns, data });


export default class Login extends Component {
    render() {
        return (

            <html>
                <body>
                    <div class="box">
                        <div class="form-center">
                        <form>
                            <h3 class = "h1"> LOG IN</h3>
                                <div class ="form-group">
                                    <label class="right-align-class">Email address</label>
                                    <input type="email" className="form-control" placeholder="Enter email" />
                                </div>

                                <div class ="form-group">
                                    <label class="right-align-class">Password</label>
                                    <input type="password" className="form-control" placeholder="Enter password" />
                                </div>
                                <div class="form-group">
                                    <button type="submit" className="btn btn-primary">Submit</button>
                                </div>
                                <p class="form-group">
                                    No Login? <a href="#">Sign Up.</a>
                                </p>
                            
                        </form>
                        </div>
                    </div>
                </body>
            </html>
        );
    }
}

