import React, { } from 'react';
import '../../styles/tableCSS.css';
import CompanyRow from './CompanyRow';
import './companies.css'

// check companies class
export default class Companies extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      companies: []
    }
    this.getCompanies();
  }

  getCompanies = () => {
    fetch("/companies")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            companies: result.tableData
          });
        },
        (error) => {
          this.setState({
            error
          });
        }
      )
  }

  render() {
    return <div className='table-container'>
      <div className='title'>
          <h1 className="h1">Companies</h1>
      </div>
      <table class="center">
        <thead>
          <tr>
            <th>Company</th>
            <th>Contacts</th>
            <th>Job Matches</th>
          </tr>
        </thead>
        <tbody>
        {this.state.companies.map(element =>
                    <CompanyRow onRefresh={this.getCompanies} key={element.companyid} {...element}/>
            )}
        </tbody>
      </table>
    </div>

  }
}
