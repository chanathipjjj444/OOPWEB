import React,{useEffect, useState} from 'react'
import Layout from '../component/Layout/Layout'
import axios from 'axios';
import { useRoom } from '../context/room';
import { useNavigate } from 'react-router-dom';

const Showroom = () => {
  const Navigate = useNavigate();
  const [data,setData] = useState("")
  const [roomdata,setRoomdata]= useRoom()
  


  const handlesubmit = (e) => {
    
    e.preventDefault();
    axios.post('http://localhost:8000/findaddon/',{'numroom':data})
    .then(res=>{
    Navigate('/addon')
  })
    
  };


  return (
    <Layout>
        

        <div className='p-5 bg-light'>
          <div className='bg-white shadow border'>
          <p className='text-black'>{JSON.stringify(roomdata, null, 4)}</p>
          {/* <p className='text-black'>{JSON.stringify(insert, null, 4)}</p> */}
          <form onSubmit={handlesubmit}>
            <h4 className="title">Choose Room</h4>
            <div className="mb-3">
              <input
                type="text"
                value={data}
                onChange={event => setData(event.target.value)}
                className="form-control"
                id="exampleInputEmail1"
                placeholder="Enter Room Number"
                required
                autoFocus
              />
            </div>
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
        </form>
            {/* <table className='table'>
              <thead>
                <tr>
                    <th>Number Room</th>
                    <th>Type Room</th>
                    <th>Price Room</th>
            
                </tr>
              </thead>
              <tbody>
                {newroomdata.map((d,i)=>(
                  <tr key={i}>
                    <td>{d.Number1}</td>
                    <td>{d.Type1}</td>
                    <td>{d.Price1}</td>
                  </tr>
                ))}
              </tbody>
            </table> */}
          </div>
        </div>




        {/* <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
  <div className="col">
    <div className="card shadow-sm">
    <img src='https://patreeda.com/wp-content/uploads/2020/11/cover-nologo.jpg'    width={550} height={350} />
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white" onClick={() => Navigate("/addon")}>
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  
  <div className="col">
    <div className="card shadow-sm">
    <img src='https://s359.thaibuffer.com/rq/580/435/50/pagebuilder/dfec4bba-0663-46a2-8c90-956b8e3adaf1.jpg'    width={550} height={350} />
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white" onClick={() => Navigate("/addon")}>
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
    <img src='https://assets.lh.co.th/image/upload/f_auto,fl_lossy,q_auto/website-pro/living-tip/null/wyswyg/%E0%B9%84%E0%B8%AD%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%AB%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%99%E0%B8%AD%E0%B8%99%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%AA%E0%B8%B9%E0%B8%87%E0%B8%A7%E0%B8%B1%E0%B8%A2%20%E0%B8%AD%E0%B8%A2%E0%B8%B9%E0%B9%88%E0%B8%AA%E0%B8%9A%E0%B8%B2%E0%B8%A2%20%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%94%E0%B8%A0%E0%B8%B1%E0%B8%A2_6_1656315563904'   width={550} height={350} />
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-white bg-black text-white" onClick={() => Navigate("/addon")}>
              Submit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
      <svg
        className="bd-placeholder-img card-img-top"
        width="100%"
        height={225}
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-label="Placeholder: Thumbnail"
        preserveAspectRatio="xMidYMid slice"
        focusable="false"
      >
        <title>Placeholder</title>
        <rect width="100%" height="100%" fill="#55595c" />
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">
          Thumbnail
        </text>
      </svg>
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-secondary">
              View
            </button>
            <button type="button" className="btn btn-sm btn-outline-secondary">
              Edit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
      <svg
        className="bd-placeholder-img card-img-top"
        width="100%"
        height={225}
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-label="Placeholder: Thumbnail"
        preserveAspectRatio="xMidYMid slice"
        focusable="false"
      >
        <title>Placeholder</title>
        <rect width="100%" height="100%" fill="#55595c" />
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">
          Thumbnail
        </text>
      </svg>
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-secondary">
              View
            </button>
            <button type="button" className="btn btn-sm btn-outline-secondary">
              Edit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
      <svg
        className="bd-placeholder-img card-img-top"
        width="100%"
        height={225}
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-label="Placeholder: Thumbnail"
        preserveAspectRatio="xMidYMid slice"
        focusable="false"
      >
        <title>Placeholder</title>
        <rect width="100%" height="100%" fill="#55595c" />
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">
          Thumbnail
        </text>
      </svg>
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-secondary">
              View
            </button>
            <button type="button" className="btn btn-sm btn-outline-secondary">
              Edit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
      <svg
        className="bd-placeholder-img card-img-top"
        width="100%"
        height={225}
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-label="Placeholder: Thumbnail"
        preserveAspectRatio="xMidYMid slice"
        focusable="false"
      >
        <title>Placeholder</title>
        <rect width="100%" height="100%" fill="#55595c" />
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">
          Thumbnail
        </text>
      </svg>
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-secondary">
              View
            </button>
            <button type="button" className="btn btn-sm btn-outline-secondary">
              Edit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
      <svg
        className="bd-placeholder-img card-img-top"
        width="100%"
        height={225}
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-label="Placeholder: Thumbnail"
        preserveAspectRatio="xMidYMid slice"
        focusable="false"
      >
        <title>Placeholder</title>
        <rect width="100%" height="100%" fill="#55595c" />
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">
          Thumbnail
        </text>
      </svg>
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-secondary">
              View
            </button>
            <button type="button" className="btn btn-sm btn-outline-secondary">
              Edit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div className="col">
    <div className="card shadow-sm">
      <svg
        className="bd-placeholder-img card-img-top"
        width="100%"
        height={225}
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-label="Placeholder: Thumbnail"
        preserveAspectRatio="xMidYMid slice"
        focusable="false"
      >
        <title>Placeholder</title>
        <rect width="100%" height="100%" fill="#55595c" />
        <text x="50%" y="50%" fill="#eceeef" dy=".3em">
          Thumbnail
        </text>
      </svg>
      <div className="card-body">
        <p className="card-text">
          This is a wider card with supporting text below as a natural lead-in
          to additional content. This content is a little bit longer.
        </p>
        <div className="d-flex justify-content-between align-items-center">
          <div className="btn-group">
            <button type="button" className="btn btn-sm btn-outline-secondary">
              View
            </button>
            <button type="button" className="btn btn-sm btn-outline-secondary">
              Edit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div> */}

    </Layout>
  )
}

export default Showroom