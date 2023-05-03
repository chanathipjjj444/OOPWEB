import React from 'react'
import Layout from '../component/Layout/Layout'
import { useState } from 'react'
import axios from 'axios'

const CreateRoom = () => {

    const [namehotel,setNamehotel] = useState('')
    const [numroom,setNumroom] = useState('')
    const [types,setTypes] = useState('')
    const [priceroom,setPriceroom] = useState('')
    const [numpeople,setNumpeople] = useState('')
    const [facs,setFacs] = useState('')
    const [bedtype,setBedtype] = useState('')
    const [roompicture,setRoompicture] = useState('')
    const [statusroom,setStatusroom] = useState(false)
    const [data,setData] = useState([])

    const handlesubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/manageroom/',{'namehotel':namehotel,'numroom':numroom,'types':types,'numpeople':numpeople,'priceroom':priceroom,'facs':facs,'bedtype':bedtype,'roompicture':roompicture,'statusroom':statusroom})
        .then(res => {console.log(res)
        
        })
        axios.get('http://localhost:8000/showroom/').then(res=> {console.log(res)
        setData(res.data)
        }
        )

    }


  return (
    <Layout title={"Dashboard - Create Category"}>
        <div className='container-fluid e-3 p-3'>

        <div className='row'>
            {/* <div className='col-md-3'>
                <AdminDashboard/>
            </div> */}
            <div className='col-md-9'>
                <h1>Manage Room</h1>
                <form onSubmit={handlesubmit}>
                    <h4 className="title">Add Room</h4>
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
                        value={numroom}
                        onChange={event => {
                            setNumroom(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Numroom"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={types}
                        onChange={event => {
                            setTypes(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Type Room"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={numpeople}
                        onChange={event => {
                            setNumpeople(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Numpeople"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={priceroom}
                        onChange={event => {
                            setPriceroom(event.target.value)
                        }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Price Room"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={facs}
                        onChange={event => {
                            setFacs(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Facility"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={bedtype}
                        onChange={event => {
                            setBedtype(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter Bedtype"
                        required
                        autoFocus
                    />
                    </div>
                    <div className="mb-3">
                    <input
                        type="text"
                        value={roompicture}
                        onChange={event => {
                            setRoompicture(event.target.value)
                          }}
                        className="form-control"
                        id="exampleInputEmail1"
                        placeholder="Enter src image room"
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
                    <th scope="col">Data Rooms</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((item, index)=> (
                    // <div key={index}>
                        <>
                        <tr>
                            {/* <td><div key={index}></div></td> */}
                            <td>
                                    <p>Room Number: {item.roomnum} Type: {item.Type} NumPeople: {item.numpeople} Price: {item.price} facs: {item.facs} BedType: {item.bedtype} Status: {item.status}</p>
                                    
                                    
                                <img src={item.picture}    width={500} height={350} />

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

export default CreateRoom