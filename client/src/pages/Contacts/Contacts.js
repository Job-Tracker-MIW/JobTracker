import React, { } from 'react';
import '../../styles/tableCSS.css';
import ContactAdd from './ContactsAdd';
import ContactRow from './ContactsRow';
import './contacts.css'

export default class Contacts extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      error: null,
      contacts: []
    }
    this.getContacts();
  }

  getContacts = () => {
    const options = {
      method: 'GET',
      headers: {'token': localStorage.getItem('token')}
    }
    fetch("/contacts", options)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            contacts: result.tableData
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
          <h1 className="h1">Contacts</h1>
      </div>
      <table class="center">
        <thead>
          <tr>
            <th>Contact</th>
            <th>email</th>
            <th>phone</th>
            <th>company</th>
            <th>jobCount</th>
          </tr>
        </thead>
        <tbody>
        {this.state.contacts.map(element =>
                    <ContactRow onRefresh={this.getContacts} key={element.contactid} {...element}/>
            )}
            <ContactAdd onRefresh={this.getContacts}></ContactAdd>
        </tbody>
      </table>
    </div>

  }
}
