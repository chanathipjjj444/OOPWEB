import React,{useState} from 'react'
import { NavLink,useNavigate} from 'react-router-dom'
import {Modal}from 'antd'
import ReserveForm from '../../pages/ReserveForm'
import { useAuth } from "../../context/auth"
import axios from 'axios'

const Header = () => {
  const [visible, setVisible] = useState(false);
  const [auth, setAuth] = useAuth()




  return (
    <nav className="navbar navbar-expand-lg  bg-dark">
  <div className="container-fluid">
    <a className="navbar-brand text-white" href="#">
      🏢Hotel.com
    </a>
    <button
      className="navbar-toggler "
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span className="navbar-toggler-icon" />
    </button>
    <div className="collapse navbar-collapse" id="navbarNav">
      <ul className="navbar-nav">
        <li className="nav-item">
            <NavLink to="/" className="nav-link text-white">
            Home 
            </NavLink>
        </li>
        <li className="nav-item">
            <NavLink to="/login" className="nav-link text-white">
            Login
            </NavLink>
        </li>
        <li className="nav-item">
            <NavLink to="/register" className="nav-link text-white">
            Register 
            </NavLink>
        </li>
        <li className="nav-item">
            <NavLink to="/showhotel" className="nav-link text-white">
            CheckHotel 
            </NavLink>
        </li>

        { auth.auth ==="true" ? (<>
        <li className="nav-item">
            <NavLink to="/admin" className="nav-link text-white">
            Admin 
            </NavLink>
        </li>
        </>
        ):(<></>)}

        <li className="nav-item">
        <button
        className="btn btn-primary ms-2"
        onClick={() => {
          setVisible(true);
        }}
      >
        Reserve 🏢Hotel
      </button>
        </li>
      <li className="nav-item">
        <p className='text-white'>{JSON.stringify(auth, null, 4)}</p>
      </li>
      </ul>
    </div>
  </div>
  <Modal
  onCancel={() => setVisible(false)}
  footer={null}
  visible={visible}
>
   <ReserveForm/>
  </Modal>
</nav>


  )
}

export default Header