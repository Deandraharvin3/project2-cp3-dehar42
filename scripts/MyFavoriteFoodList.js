
export function foodList(favs) {
    return favs.map((a, index) =>
            <li className="number-item" key={index}>{a}</li>
        );
  }
