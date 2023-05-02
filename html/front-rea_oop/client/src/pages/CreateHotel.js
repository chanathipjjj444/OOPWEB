import React from 'react'
import Layout from '../component/Layout/Layout';
import AdminDashboard from './AdminDashboard';
import { useState,useEffect } from 'react';
import axios from 'axios';

const CreateHotel = () => {
    
        const [data,setData] = useState([])
        const [hotelname,setHotelname] = useState('')
        const [rating,setRating] = useState('')
        const [numsroom,setNumsroom] = useState('')
        const [hotelpicture,setHotelpicture] = useState('')
        const [location,setLocation] = useState('')
        const [province,setProvince] = useState('')
        axios.get('http://localhost:8000/showhotel/').then(res => {console.log(res)
        setData(res.data)
    })

    useEffect(() => {
        async function Showhotel() {
            const result =await axios.get('http://localhost:8000/showhotel/')
            setData(result.data);
        }
        Showhotel();
    },[])


    const handlesubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/managehotel/',{'hotelname':hotelname,'rating':rating,'numsroom':numsroom,'hotelpicture':hotelpicture,'location':location,'province':province})
        .then(res => {console.log(res)})

    }


  return (
    <Layout title={"Dashboard - Create Category"}>
        <div className='container-fluid e-3 p-3'>

        <div className='row'>
            {/* <div className='col-md-3'>
                <AdminDashboard/>
            </div> */}
            <div className='col-md-9'>
                <h1>Manage Hotel</h1>
                <form onSubmit={handlesubmit}>
                    <h4 className="title">Add Hotel</h4>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={hotelname}
                        onChange={event => {
                            setHotelname(event.target.value)
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
                        value={rating}
                        onChange={event => {
                            setRating(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Rating Hotel"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={numsroom}
                        onChange={event => {
                            setNumsroom(event.target.value)
                        }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Nums Room"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={hotelpicture}
                        onChange={event => {
                            setHotelpicture(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Src Image"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={location}
                        onChange={event => {
                            setLocation(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Location"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={province}
                        onChange={event => {
                            setProvince(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Sublocation"
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
                    {/* <th scope="col">Index</th> */}
                    <th scope="col">Data Hotel</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index)=> (
                    // <div key={index}>
                        <>
                        <tr>
                            {/* <td><div key={index}></div></td> */}
                            <td>
                                    <p>{item.Name_hotel} Rating: {item.Rating} Nums_room: {item.Num_rooms} Location: {item.Location} Province: {item.Province}</p>
                                    
                                    
                                <img src={item.hotel_picture}    width={500} height={350} />

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

export default CreateHotel