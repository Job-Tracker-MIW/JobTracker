import React, { } from 'react';
import '../../styles/tableCSS.css';
import AppliedJobsAdd from './AppliedJobsAdd';
import AppliedJobsRow from './AppliedJobsRow';
import './AppliedJobs.css'

export default class AppliedJobs extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      AppliedJobs: [],
    }
    this.getAppliedJobs();
  }

  getAppliedJobs = () => {
    const options = {
      method: 'GET',
      headers: {'token': localStorage.getItem('token')}
    }
    fetch("/appjobs", options)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            AppliedJobs: result.tableData
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
          <h1 className="h1">Applied Jobs</h1>
      </div>
      <table class="center">
        <thead>
          <tr>
            <th>Title</th>
            <th>Company</th>
            <th>User defined name</th>
            <th>Application Date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
        {this.state.AppliedJobs.map(element =>
                    <AppliedJobsRow onRefresh={this.getAppliedJobs} key={element.appid} {...element}/>
            )}
            <AppliedJobsAdd onRefresh={this.getAppliedJobs} {...this.state.AppliedJobs[0]}></AppliedJobsAdd>
        </tbody>
      </table>
    </div>

  }
}
