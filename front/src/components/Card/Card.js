import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

const styles = {
  card: {
    minWidth: "80%",
    margin: "24px 32px 8px 32px",
    padding: "16px"
  },
  bullet: {
    display: "inline-block",
    margin: "0 2px",
    transform: "scale(0.8)"
  },
  title: {
    fontSize: 14
  },
  pos: {
    marginBottom: 12
  },
  button: {
    backgroundColor: "#42a5f5",
    color: "white"
  },
  header: {
    margin: "16px",
    textAlign: "center"
  },
  btnHolder: {
    display: "grid",
    gridTemplateRows: "1fr 1fr",
    gridTemplateColumns: "1fr 1fr",
    gridColumnGap: "32px",
    gridRowGap: "32px"
  }
};

function SimpleCard(props) {
  const { classes } = props;
  const answers = props.answers;
  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography
          className={classes.title}
          color="textSecondary"
          gutterBottom
        >
          Вопрос № {props.number}
        </Typography>
        <Typography variant="h5" component="h2" className={classes.header}>
          {props.name}
        </Typography>
        <div className={classes.btnHolder}>
          {answers.map(ans => {
            return (
              <Button
                variant="contained"
                className={classes.button}
                key={ans.id}
              >
                {ans.value}
              </Button>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}

SimpleCard.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(SimpleCard);
