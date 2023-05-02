import React, { useState } from 'react'
import Layout from '../component/Layout/Layout'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const PeopleForm = () => {
  const [totalprice,setTotalPrice] = useState("")
  const [numcard,setNumcard] = useState('')
  const [cvv,setCvv] = useState('')
  const [coupon,setCoupon] = useState('')
  const Navigate = useNavigate()

  axios.get('http://localhost:8000/totalprice/')
    .then(res=>{
      setTotalPrice(
        res.data.total_price
      )
    })
  
    const handlesubmit = (e) => {
    
      e.preventDefault();
      axios.post('http://localhost:8000/payment/',{'numcard':numcard,'cvv':cvv,'coupon':coupon})
      .then(res=>{
      Navigate('/billupdate')
    })
      
    };


  return (
    <Layout title="Insert-data">
    <div className="form-container" style={{ minHeight: "85vh" }}>
      <form onSubmit={handlesubmit}>


        <h4>Payment</h4>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            value={numcard}
            onChange={event => {
              setNumcard(event.target.value)
            }}
            
            placeholder="Insert Number Card"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            value={cvv}
            onChange={event => {
              setCvv(event.target.value)
            }}
            
            placeholder="Insert CVV"
            required
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            value={coupon}
            onChange={event => {
              setCoupon(event.target.value)
            }}
           
            placeholder="Insert Coupon"
            required
          />
        </div>
        <p className='text-black'>Price Payment : {totalprice}</p>
        
        <button type='submit' className="btn btn-primary ms-2">
            ACCEPT PAYMENT
        </button>
        
      </form>
    </div>
  </Layout>
  )
}

export default PeopleForm