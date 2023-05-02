import React,{ useEffect, useState} from 'react'
import Layout from '../component/Layout/Layout'
import room3 from '../pages/image/room3.jpg'
import axios from 'axios'


const HomePage = () => {


  return (
    <Layout>

    <body className='bg-dark-subtle' style={{minHeight:"80vh"}}>

    <div
      className="bg-image"
      style={{
        backgroundImage:
          'url("https://imgcp.aacdn.jp/img-a/1720/auto/global-aaj-front/article/2019/12/5df85adc8ad28_5df85ad1c3c84_818801298.jpg")',
        height: 800
      }}
    >
      <h1 className='text-center font-italic text-white'>
        <br/>
        HOTEL
      </h1>
      <h1 className='text-center font-italic'>OOP<br/><br/><br/><br/></h1>

      <div className="container ">
        <div className="row">
          <div className="col-lg-3 col-md-12 mb-4 mb-lg-0  ">
            {/* Card */}
            <div
              className="bg-image card shadow-1-strong"
              style={{
                backgroundImage:
                  'url("https://mdbootstrap.com/img/new/slides/003.jpg")'
              }}
            >
              <div className="card-body text-white ">
                <h5 className="card-title">About</h5>
                <p className="card-text">
                  some
                </p>
                <a href="#!" className="btn btn-outline-light">
                  check
                </a>
              </div>
            </div>
            {/* Card */}
          </div>
          <div className="col-lg-3 mb-4 mb-lg-0 ">
            {/* Card */}
            <div
              className="bg-image card shadow-1-strong"
              style={{
                backgroundImage:
                  'url("https://mdbootstrap.com/img/new/slides/028.jpg")'
              }}
            >
              <div className="card-body text-white">
                <h5 className="card-title">FAQ</h5>
                <p className="card-text">
                  some
                </p>
                <a href="#!" className="btn btn-outline-light">
                  check
                </a>
              </div>
            </div>
            {/* Card */}
          </div>

        </div>
      </div>

    </div>




</body>

    </Layout>
  )
}

export default HomePage