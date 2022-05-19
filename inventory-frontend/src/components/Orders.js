import { useEffect, useState } from "react"
import { Wrapper } from "./Wrapper"

export const Orders = () => {
    /* variables declaration */
    const [id, setId] = useState('');
    const [quantity, setQuantity] = useState('');
    const [message, setMessage] = useState('Buy your favorite product');

    useEffect(() => {
        (async () => {
            try{
                if(id) {
                    const response = await fetch(`http://localhost:8000/products/${id}`);
                    const content = await response.json();
                    setMessage(`Product price : $${content.price}`); 
                }                
            } catch (e) {
                setMessage('Buy your favorite product')
            }
        })();
    }, [id]);
    /* submit function declaration */
    const submit = async e => {
        e.preventDefault();

        await fetch('http://localhost:8001/orders', {
            method: 'POST',
            mode: 'no-cors',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                id,
                quantity
            })
        });
        
        setMessage('Thank you for your order!');
    }
    return <Wrapper>
    <div className="Container">
        <main>
            <div className="py-5 text-center">
                <h2>
                    Checkout form
                </h2>
                <p className="lead">{message}</p>
            </div>

            <form onSubmit={submit}>
                <div className="row g-3">
                    <div className="col-sm-6">
                        <label className="form-label">Product</label>
                        <input className="form-control" onChange={e => setId(e.target.value)}/>
                    </div>

                    <div className="col-sm-6">
                        <label className="form-label">Quantity</label>
                        <input type="number" className="form-control" onChange={e => setQuantity(e.target.value)}/>
                    </div>
                 </div>

                <hr className="my-4"/>
                <button className="w-100 btn btn-primary btn-lg" type="submit">Buy</button>
            </form>
        </main>
    </div>
    </Wrapper>
}