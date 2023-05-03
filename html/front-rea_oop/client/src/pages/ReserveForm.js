import React, { useState } from 'react'
import { NavLink, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useRoom } from '../context/room';
import { useSystem } from '../context/system';
// import { useData } from '../context/data';


const ReserveForm = () => {

  const [country,setCountry] = useState("")
  const [hotel,setHotel] = useState("")
  const [room,setRoom] = useState("")
  const [people,setPeople] = useState("")
  const [checkin,setCheckin] = useState("")
  const [checkout,setCheckout] = useState("")
  const [roomdata,setRoomdata]= useRoom()
  const [t,setT] = useState("")
  const [auth,setAuth] = useState('')

  // const [insert,setInsert] = useData()
  const Navigate = useNavigate();
  
  axios.get('http://localhost:8000/auth/')
  .then(res=>setAuth(res.data.message))

  const handlesubmit = (e) => {
    if(auth === 'success'){
      e.preventDefault();
      axios.post('http://localhost:8000/findavailableroom/',{'country':country,'hotel':hotel,'room':room,'people':people,'checkin':checkin,'checkout':checkout})
    .then(res => {

    setRoomdata({
      ...roomdata,
      FreeRoom: res.data
    })
    Navigate('/showroom')
  
    })

    }
  };



  return (
    <>
      
      

      <form onSubmit={handlesubmit}>
          <div className="form-input">
            <select
              className="input-field master s2 _js-affectsProperties select2-hidden-accessible"
              data-select2-id="select2-data-1-dhga"
              tabIndex={-1}
              aria-hidden="true"
              value={country}
              onChange={event => {
                setCountry(event.target.value)
              }}
          >
          <option data-invalid="" data-select2-id="select2-data-3-u6jo">
            Please Select
          </option>
          <option value="Thailand" data-filteropts="thailand">
            Thailand
          </option>
          {" "}
        </select>
        <span
          className="select2 select2-container select2-container--default"
          dir="ltr"
          data-select2-id="select2-data-2-4clg"
          style={{ width: "496.031px" }}
        >
          <span className="selection">
            <span
              className="select2-selection select2-selection--single"
              role="combobox"
              aria-haspopup="true"
              aria-expanded="false"
              tabIndex={0}
              aria-disabled="false"
              aria-labelledby="select2-culu-container"
            >
              <span
                className="select2-selection__rendered"
                id="select2-culu-container"
                role="textbox"
                aria-readonly="true"
                title="Please Select"
              >
                Please_Select_
              </span>
              <span className="select2-selection__arrow" role="presentation">
                <b role="presentation" />
              </span>
            </span>
          </span>
          <span className="dropdown-wrapper" aria-hidden="true" />
        </span>
        <label className="select-label" htmlFor="hotel-country">
          <span className="label">Country</span>
        </label>
      </div>
      <div className="form-input">
        <div className="form-input--stepper">
          <label>Hotel name</label>
          <input
            name="hotel"
            className="input-field"
            type="string"
            value={hotel}
            onChange={event => {
              setHotel(event.target.value)
            }}
          />
        </div>
      </div>
      <div className="form-input">
        <div className="form-input--stepper">
          <label>Room</label>
          <input
            name="room"
            className="input-field"
            type="number"
            min={0}
            max={4}
            defaultValue={0}
            value={room}
            onChange={event => {
              setRoom(event.target.value)
            }}
          />
        </div>
      </div>
      <div className="form-input">
        <div className="form-input--stepper">
          <label>People</label>
          <input
            name="people"
            className="input-field"
            type="number"
            min={0}
            max={4}
            defaultValue={0}
            value={people}
            onChange={event => {
              setPeople(event.target.value)
            }}
          />
        </div>
      </div>

      <div className="form-input">
        <div className="form-input--stepper">
          <label>CheckIn</label>
          <input
            defaultValue={"27-4-2023"}
            name="checkin"
            className="input-field"
            type="string"
            value={checkin}
            onChange={event => {
              setCheckin(event.target.value)
            }}
          />
        </div>
      </div>

      <div className="form-input">
        <div className="form-input--stepper">
          <label>CheckOut</label>
          <input
            name="checkout"
            className="input-field"
            type="string"
            value={checkout}
            onChange={event => {
              setCheckout(event.target.value)
            }}
          />
        </div>
      </div>

      {/* <div className="row">
        <div className="form-group">
          <label>Day</label>
          <select className="form-control select2" style={{ width: "100%" }}>
            <option selected="selected">1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
            <option>9</option>
            <option>10</option>
            <option>11</option>
          </select>
        </div>
      </div>
      <div className="row">
        <div className="form-group">
          <label>Month</label>
          <select className="form-control select2" style={{ width: "100%" }}>
            <option selected="selected">1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
            <option>9</option>
            <option>10</option>
            <option>11</option>
            <option>12</option>
          </select>
        </div>
      </div>
      <div className="row">
        <div className="form-group">
          <label>Year</label>
          <select className="form-control select2" style={{ width: "100%" }}>
            <option selected="selected">2023</option>
            <option>2024</option>
            <option>3025</option>
            <option>2026</option>
            <option>2027</option>
          </select>
        </div>
      </div> */}




        <button type="submit" className="btn btn-primary">
            {/* <NavLink to="/showroom" className="nav-link"> */}
            Submit
            {/* </NavLink> */}
        </button>
      </form>
    </>
  )
}

export default ReserveForm