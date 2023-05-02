import React, { useState } from 'react'
import Layout from '../component/Layout/Layout'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { toast } from 'react-toastify';


const Bill = () => {
    const Navigate = useNavigate()
    const [balance,setBalance] = useState('')
    const [message,setMesagge] = useState('')
    axios.get('http://localhost:8000/bill/')
    .then(res =>{
        setBalance(res.data.new_balance)
        setMesagge(res.data.message)
    } )

  const handlesubmit = (e) => {
    e.preventDefault();
    axios.get('http://localhost:8000/updatebill/')
  .then(res =>{ 
    setTimeout( () => {
        toast.success('Reserve Success')}
      ,3000)
    Navigate('/')
    })
  };


  return (
    <Layout title="Bill-Payment">
      <div className="form-container " style={{ minHeight: "85vh" }}>
        <form onSubmit={handlesubmit}>
          <h4 className="title">Bill-Payment</h4>
          
          <div className="mb-3 text-black">
           {message}
          </div>
          <div className="mb-3 text-black">
            Your balance : {balance}
          </div>

          <button type="submit" className="btn btn-primary">
            Accept
          </button>
        </form>
      </div>
    </Layout>

  )
}

export default Bill