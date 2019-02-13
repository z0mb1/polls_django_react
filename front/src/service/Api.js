fetch(this.props.endpoint)
  .then(response => {
    if (response.status !== 200) {
      return this.setState({ placeholder: "Something went wrong" });
    }
    return response.json();
  })
  .then(data => this.setState({ data: data, loaded: true }));
