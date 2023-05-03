import React, { useState } from 'react'
import Layout from '../component/Layout/Layout'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useData } from '../context/data'
import { useLast } from '../context/lastprice'
import { useAddons } from '../context/addonsshow'


const Addon = () => {
    const Navigate = useNavigate();
    const [servicetype,setServicetype] = useState('')
    const [nameservice,setNameservice] = useState('')
    const [prices,setPrices] = useData()
    const [type,setType] = useState('')
    const [lprice,setLprice]= useLast()
    const [price, setPrice] = useState("")
    const [addonsdata,setAddonsdata] = useAddons([])
    const [data,setData] = useState([])

    axios.get('http://localhost:8000/bookroom/')
    .then(res=>{
      setPrice(
        res.data.Price
      )
    })

    // axios.get('http://localhost:8000/getaddons/').then(res=> {console.log(res)
    //     setData(res.data)
    //     }
    //     )
      


const handlesubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/addon/',{'servicetype':servicetype,'nameservice':nameservice})
  .then(res => {if(res.data.message === "success"){
      Navigate('/insertdata')
  }
})
}

  return (

    <Layout>
        
        <p className='text-black'>{JSON.stringify(addonsdata, null, 4)}</p>
    <div className="form-container" style={{ minHeight: "85vh" }}>
        <form onSubmit={handlesubmit}>
            <h4 className="title">Addons FORM</h4>
            <div className="mb-3">
            <input
                type="text"
                value={servicetype}
                onChange={event => setServicetype(event.target.value)}
                className="form-control"
                
                placeholder="Enter Type service"
                required
                autoFocus
            />
            </div>
            <div className="mb-3">
            <input
                type="text"
                value={nameservice}
                onChange={event => setNameservice(event.target.value)}
                className="form-control"
            
                placeholder="Enter Your Name service "
                required
            />
            </div>
            
            <p className='text-black'>TotalPrice Now : {price}</p>
            <button type="submit" className="btn btn-primary">
            Submit
            </button>
        </form>
        </div>




    {/* <div className='row'>
        
        <div className="card" style={{ width: "35rem" }}>
        <img src="https://s.isanook.com/he/0/ud/2/11101/breakfast.jpg" className="card-img-top"/>
        <div className="card-body">
            <h5 className="card-title">ฺBreakFast Service</h5>
            <p className="card-text">
            Some quick example text to build on the card title and make up the bulk of
            the card's content.00
            </p>
        </div>
        <div className="card-body">
        <form onSubmit={handlesubmit}>
        <div className="mb-3">
            <input
              type="text"
              value={type}
              onChange={event => 
              setType(event.target.value)
              }
              className="form-control"
              id="exampleInputEmail1"
              placeholder="Enter Your Breakfast "
              required
            />
            <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </div>
        </form>
        </div>
        </div>

        <div className="card" style={{ width: "35rem" }}>
        <img src="https://s.isanook.com/au/0/rp/rc/w670h402/yatxacm1w0/aHR0cHM6Ly9zLmlzYW5vb2suY29tL2F1LzAvdWQvMTQvNzA3MDkvMC5qcGc=.jpg" className="card-img-top"/>
        <div className="card-body">
            <h5 className="card-title">Car Service</h5>
            <p className="card-text">
            Some quick example text to build on the card title and make up the bulk of
            the card's content.
            </p>
        </div>
        
        <div className="card-body">
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white m-3" >
                Add
            </button>
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white" >
                No
            </button>
        </div>
        </div>

        <div className="card" style={{ width: "35rem" }}>
        <img src="https://static.wixstatic.com/media/c8a905_d5b5222b12df448bb0c7681b9be94757~mv2.jpg/v1/fill/w_640,h_426,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/c8a905_d5b5222b12df448bb0c7681b9be94757~mv2.jpg" className="card-img-top"/>
        <div className="card-body">
            <h5 className="card-title">Spa Service</h5>
            <p className="card-text">
            Some quick example text to build on the card title and make up the bulk of
            the card's content.
            </p>
        </div>
        
        <div className="card-body">
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white m-3" >
                Add
            </button>
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white" >
                No
            </button>
        </div>
        </div>   

        <div className="card" style={{ width: "35rem" }}>
        <div className="card-body">
            <h5 className="card-title">Update Addons</h5>
            <p className='text-black'>
            Totalprice : {totalprice}
            </p>
            <button type='button' className="btn btn-sm btn-outline-white bg-black text-white" onClick={() => Navigate("/insertdata")}>
            Accept Update            
            </button>

        </div>
        </div>

    </div> */}


    </Layout>

  )
}

export default Addon