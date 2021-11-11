import ReactDOM from 'react-dom';

export const validateNotBlank = (userdata) => {
    for (const property in userdata) {
        if (userdata[property].length === 0) {
            const element = <p className="incorrect-text">One or more fields are blank</p>;
            ReactDOM.render(element, document.getElementsByClassName('incorrect-creds')[0]);
            return false 
    }
    return true
    }
}

export const validateEmail = (email) => {
    let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (reg.test(email) === false) {
        const element = <p className="incorrect-text">Invalid email format</p>;
        ReactDOM.render(element, document.getElementsByClassName('incorrect-creds')[0]);
        return false;
      }
      else {
        return true;
      }
}

export const validatePasswords = (password1, password2) =>{
    if (password1 === password2) {
        return true
    }
    const element = <p className="incorrect-text">Passwords do not match</p>;
    ReactDOM.render(element, document.getElementsByClassName('incorrect-creds')[0]);
    return false
}