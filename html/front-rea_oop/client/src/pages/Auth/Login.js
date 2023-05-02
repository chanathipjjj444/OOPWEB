import React, { useState } from 'react'
import Layout from '../../component/Layout/Layout'
import axios from 'axios'
import {toast} from 'react-toastify';

import { useNavigate } from 'react-router-dom'
import { useAuth } from '../../context/auth';
var delaymisecond = 2000;

const Login = () => {
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [auth,setAuth] = useAuth()
  const Navigate = useNavigate();

  const handlesubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/login/',{'email':email,'password':password})
  .then(res => {if(res.data.success === "true"){
    setTimeout( () => {
      toast.success('Login Success')}
    ,delaymisecond)
    setAuth({
      ...auth,
      user: res.data.name,
      email: res.data.email,
      auth: res.data.auth,
      // success: res.data.success
    })
    Navigate('/')    
  }
  else{
    toast.warn('Invalid Login')
  }
})
  };

  return (
    <Layout title="Login - Ecommer App">
      <div className="form-container " style={{ minHeight: "85vh" }}>
        <form onSubmit={handlesubmit}>
          <h4 className="title">LOGIN FORM</h4>
          
          <div className="mb-3">
            <input
              type="email"
              value={email}
              onChange={event => {
              setEmail(event.target.value)
              }}
              className="form-control"
              id="exampleInputEmail1"
              placeholder="Enter Your Email "
              required
            />
          </div>
          <div className="mb-3">
            <input
              type="password"
              value={password}
              onChange={event => {
                setPassword(event.target.value)
              }}
              className="form-control"
              id="exampleInputPassword1"
              placeholder="Enter Your Password"
              required
            />
          </div>

          <button type="submit" className="btn btn-primary">
            LOGIN
          </button>
        </form>
      </div>
    </Layout>
  )
}

export default Login