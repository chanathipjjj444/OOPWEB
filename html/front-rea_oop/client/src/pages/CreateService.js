import React from 'react'
import Layout from '../component/Layout/Layout'
import axios from 'axios'
import { useState } from 'react'

const CreateAddons = () => {

    const [type,setType] = useState('')
    const [name,setName] = useState('')
    const [detail,setDetail] = useState('')
    const [picture,setPicture] = useState('')
    const [price,setPrice] = useState('')
    const [namehotel,setNamehotel] = useState('')
    const [data,setData] = useState([])

    const handlesubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/manageaddons/',{'Typeservice':type,'Nameservice':name,'detail':detail,'picture':picture,'price':price,'namehotel':namehotel})
        .then(res => {console.log(res)})
        axios.get('http://localhost:8000/getaddons/').then(res=> {console.log(res)
        setData(res.data)
        }
        )

    }



  return (
    <Layout title={"Dashboard - Create Service"}>
        <div className='container-fluid e-3 p-3'>

        <div className='row'>
            {/* <div className='col-md-3'>
                <AdminDashboard/>
            </div> */}
            <div className='col-md-9'>
                <h1>Manage Service</h1>
                <form onSubmit={handlesubmit}>
                    <h4 className="title">Add Service</h4>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={namehotel}
                        onChange={event => {
                            setNamehotel(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Name Hotel"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={type}
                        onChange={event => {
                            setType(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Type service"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={name}
                        onChange={event => {
                            setName(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Name service"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={detail}
                        onChange={event => {
                            setDetail(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Detail"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={picture}
                        onChange={event => {
                            setPicture(event.target.value)
                        }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter src picture"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={price}
                        onChange={event => {
                            setPrice(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Price"
                        required
                        autoFocus
                    />
                    </div>
                
                    <button type="submit" className="btn btn-primary">
                    Add
                    </button>
                </form>
                <div className='w-75'>
                <table className="table">
                <thead>
                    <tr>
                    <th scope="col">Data Service</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index)=> (
                    // <div key={index}>
                        <>
                        <tr>
                            {/* <td><div key={index}></div></td> */}
                            <td>
                                    <p>{item.Hotel} Type: {item.Service_type} Name service: {item.Name} Detail: {item.Detail} Price: {item.Price}</p>
                                    
                                    
                                <img src={item.Picture}    width={500} height={350} />

                            </td>
                        </tr>
                        
                        </>
                            
                        
                    ))}
                </tbody>
                </table>

                </div>
                {/* <Modal onCancel={()=> setVisible(false)} 
                footer={null} 
                visible={visible}
                >
                    <CategoryForm value={updatedName} setValue={setUpdatedName} handleSubmit={handleUpdate}></CategoryForm>
                </Modal> */}
            </div>
        </div>

        </div>
    </Layout>
  )
}

export default CreateAddons
