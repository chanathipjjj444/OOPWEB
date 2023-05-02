import React, { useEffect, useState } from 'react'
import Layout from '../../component/Layout/Layout'
import axios from 'axios'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'
var delaymisecond = 2000

const Register = () => {

const [name,setName] = useState("");
const [email,setEmail] = useState("");
const [password,setPassword] = useState("");
const [phone,setPhone] = useState("");
const [address,setAddress] = useState("");
const Navigate = useNavigate()

// {'name':name,'email':email,'password':password,'phone':phone,'address':address}

const handlesubmit = (e) => {
  e.preventDefault();
  axios.post('http://localhost:8000/register/',{'name':name,'email':email,'password':password,'phone':phone,'address':address})
  .then(res => {if(res.data.message === "success"){
    setTimeout(()=> {
      toast.success('Register Success')
    }
    ,delaymisecond)
    Navigate("/login")
  }
  else{
    toast.warn('Invalid Register')
  }
  })
  };


  return (
    <Layout title="Register - Ecommer App">
    <div className="form-container" style={{ minHeight: "85vh" }}>
      <form onSubmit={handlesubmit}>
        <h4 className="title">REGISTER FORM</h4>
        <div className="mb-3">
          <input
            type="text"
            value={name}
            onChange={event => setName(event.target.value)}
            className="form-control"
            id="exampleInputEmail1"
            placeholder="Enter Your Name"
            required
            autoFocus
          />
        </div>
        <div className="mb-3">
          <input
            type="email"
            value={email}
            onChange={event => setEmail(event.target.value)}
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
            onChange={event => setPassword(event.target.value)}
            className="form-control"
            id="exampleInputPassword1"
            placeholder="Enter Your Password"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            value={phone}
            onChange={event => setPhone(event.target.value)}
            className="form-control"
            id="exampleInputEmail1"
            placeholder="Enter Your Phone"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            value={address}
            onChange={event => setAddress(event.target.value)}
            className="form-control"
            id="exampleInputEmail1"
            placeholder="Enter Your Address"
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          REGISTER
        </button>
      </form>
    </div>
  </Layout>
  )
}

export default Register