
Here’s the code. Note the use of requestAnimationFrame, which you supply with a function to execute 
before the next time the browser repaints.

bouncingballs.js
/*
 * A script illustrating bouncing balls. The HTML should provide a container div
 * (id = 'bounceContainer') and a button (id = 'startOrStopBounce') that toggles
 * the animation.
 */

window.addEventListener('load', () => {
  const container = document.querySelector('#bounceContainer')
  const button = document.querySelector('#startOrStopBounce')

  class Ball {
    constructor(x, y, dx, dy, diameter, color) {
      // Initial model
      Object.assign(this, { x, y, dx, dy, diameter })

      // Initial view
      this.div = document.createElement('div')
      Object.assign(this.div.style, {
        left: `${x}px`,
        top: `${y}px`,
        width: `${diameter}px`,
        height: `${diameter}px`,
        borderRadius: `${diameter / 2}px`,
        backgroundColor: color,
        position: 'absolute',
      })
      container.appendChild(this.div)
    }

    move() {
      // Update the model
      [this.x, this.y] = [this.x + this.dx, this.y + this.dy]
      if (this.x < 0 || this.x > container.clientWidth - this.diameter) {
        this.x = Math.max(0, Math.min(this.x, container.clientWidth - this.diameter))
        this.dx = -this.dx
      }
      if (this.y < 0 || this.y > container.clientHeight - this.diameter) {
        this.y = Math.max(0, Math.min(this.y, container.clientHeight - this.diameter))
        this.dy = -this.dy
      }

      // Update the view
      [this.div.style.left, this.div.style.top] = [`${this.x}px`, `${this.y}px`]
    }
  }

  const advance = () => {
    balls.forEach(ball => ball.move())
    if (button.value === 'STOP') {
      requestAnimationFrame(advance)
    }
  }

  button.addEventListener('click', () => {
    if (button.value === 'STOP') {
      button.value = 'START'
    } else {
      requestAnimationFrame(advance)
      button.value = 'STOP'
    }
  })

  const balls = [
    new Ball(20, 70, 3, 2, 30, 'rgba(90, 255, 95, 0.5)'),
    new Ball(500, 300, -3, -3, 35, 'rgba(200, 41, 199, 0.5)'),
    new Ball(140, 10, 5, 5, 40, 'rgba(250, 50, 10, 0.4)'),
  ]
})

