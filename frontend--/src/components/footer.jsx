function Footer() {
    return (
        <footer>
            <div className="row">
                <div className="col">
                    <h2>Contact Info</h2>
                    <p>Email: bearsyker@gmail.com</p>
                    <p>Phone: 1203912309124</p>
                    <h2>Socials</h2>
                </div>
                <div className="col form">
                    <div className="tx">
                        <h2>Contact Me</h2>
                        <form action="#">
                            <div class="email">
                                <div class="text">email</div>
                                <input type="email" required placeholder="your email"></input>
                            </div>
                            <div class="msg">
                                <div class="text">message</div>
                                <textarea name="name" rows="2" cols="25" required placeholder="send a message"></textarea>
                            </div>
                            <div>
                                <button className="btn" type="submit"><span class="text">Submit</span></button>
                            </div>
                        </form>
                    </div>
                </div>
                
            </div>
        </footer>
  )
}



export default Footer