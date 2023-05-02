import axios from 'axios'
import Layout from '../component/Layout/Layout'
import React, { useEffect, useState } from 'react'

const Showhotel = () => {
    const [data,setData] = useState([])
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

    
  return (
    <Layout>
        <h1>Showhotel</h1>
        <div>
            {data.map((item, index)=> (
                <div key={index}>
                    <div className='p-5 bg-light'>
                    <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                      <div className="col">
                            <div className="card shadow-sm">
                                <p>{item.Name_hotel}</p>
                                <p>Rating: {item.Rating}</p>
                                <p>Nums_room: {item.Num_rooms}</p>
                                <p>Location: {item.Location}</p>
                                <p>Province: {item.Province}</p>
                            <img src={item.hotel_picture}    width={500} height={350} />
                            <div className="card-body"> 
                                <div className="d-flex justify-content-between align-items-center">
                                <div className="btn-group">
                                    
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    {/* <p>Number: {item.Name_hotel}</p>
                    <p>Rating: {item.Rating}</p>
                    <p>Nums_room: {item.Nums_rooms}</p>
                    <p>hotel_picture: {item.hotel_picture}</p>
                    <p>Location: {item.Location}</p>
                    <p>Province: {item.Province}</p> */}
                </div>
            ))}
        </div>
        
    </Layout>
  )
}

export default Showhotel