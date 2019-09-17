import * as React from 'react';

export class MyFavoriteFoodList extends React.Component {
  render() {
    const listItems = this.props.food.map((a, index) =>
            <li className="number-item" key={index}>{a}</li>
        );
    
    return (
            <div>
                <ul>{listItems}</ul>
            </div>
        );
  }
}